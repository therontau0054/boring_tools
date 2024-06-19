import os
import json
import arxiv
import datetime


def papers_filter(papers):
    """
    Filter the papers by the doi.
    """
    papers_list_path = "./entry_id.list"
    with open(papers_list_path, 'r', encoding = "utf8") as f:
        papers_filtered_id = f.readlines()
    papers_filtered_id = [id.strip() for id in papers_filtered_id]
    papers_new = []
    with open(papers_list_path, 'a', encoding = "utf8") as f:
        for paper in papers:
            id = paper.entry_id.split('/')[-1]
            if id not in papers_filtered_id:
                f.write(id + "\n")
                papers_new.append(paper)
    return papers_new

def search_by_keyword(keyword: str, max_results: int) -> list:
    """
    Search arXiv by keyword and return the results.
    """
    client = arxiv.Client()
    search = arxiv.Search(
        query = keyword + " AND cat:cs.AI",
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    papers = papers_filter(client.results(search))
    return papers


def get_paper_authors(paper):
    authors = []
    for author in paper.authors:
        authors.append(author.name)
    authors = ", ".join(authors)
    return authors



def save_to_json(papers):
    """
    Save the papers to a JSON file.
    """
    dir = "./papers_metadata"
    os.makedirs(dir, exist_ok = True)
    date = str(datetime.date.today()).replace("-", "")[2:]
    file_path = f"{dir}/papers_{date}.json"
    papers_metadata = {}
    for k, v in papers.items():
        papers_metadata[k] = []
        for paper in v:
            paper_metadata = {
                "title": paper.title,
                "authors": get_paper_authors(paper),
                "summary": paper.summary,
                "pdf_url": paper.pdf_url,
                "published": str(paper.published),
                "updated": str(paper.updated),
            }
            papers_metadata[k].append(paper_metadata)
    with open(file_path, 'w', encoding = "utf8") as file:
        json.dump(papers_metadata, file, indent = 4)
    return papers_metadata


def dict_to_md(papers_metadata):
    """
    Convert the papers metadata to a Markdown file.
    """
    file_name = "README.md"
    abstract_dir = "./papers_abstract"
    os.makedirs(abstract_dir, exist_ok = True)
    date = str(datetime.date.today())
    abstract_path = f"{abstract_dir}/abstracts_{date.replace('-', '')[2:]}.md"
    with open(file_name, 'r', encoding = "utf8") as file:
        lines = file.readlines()

    # 找到第一个二级标题的位置
    insert_index = 0
    for i, line in enumerate(lines):
        if line.startswith("## "):
            insert_index = i
            break
    insert_index = len(lines) if insert_index == 0 else insert_index

    # 插入新的二级标题
    new_content = f"\n## Update on {date}\n"

    f = open(abstract_path, 'w', encoding = "utf8")
    f.write(f"# Abstracts of Papers\n\n")
    abstracts_content = ""
    # keyword 作为三级标题
    for k, v in papers_metadata.items():
        new_content += f"\n### {k}\n"
        new_content += "|Publish Date|Title|Authors|PDF|\n"
        new_content += "|---|---|---|---|\n"
        for paper_metadata in v:
            published_date = paper_metadata['published'].split()[0]
            updated_date = paper_metadata['updated'].split()[0]
            title = paper_metadata['title']
            authors = paper_metadata['authors']
            pdf_url = paper_metadata['pdf_url']
            pdf_id = pdf_url.split('/')[-1]

            abstract = paper_metadata['summary']
            abstracts_content += f"## {title}\n"
            abstracts_content += f"**Authors**: {authors}\n\n"
            abstracts_content += f"**Published Date**: {published_date}\n\n"
            abstracts_content += f"**Updated Date**: {updated_date}\n\n"
            abstracts_content += f"**PDF Url**: [{pdf_id}]({pdf_url})\n\n"
            abstracts_content += f"**Abstract**: {abstract}\n\n\n"

            new_content += f"|{published_date}"
            new_content += f"|{title}"
            new_content += f"|{authors.split(', ')[0]}"
            new_content += f"|[{pdf_id}]({pdf_url})|\n\n"
    f.write(abstracts_content)
    f.close()

    # 更新 README.md 文件
    lines.insert(insert_index, new_content)
    with open(file_name, 'w', encoding = "utf8") as file:
        file.writelines(lines)


def json_to_md(json_path):
    """
    Convert the papers metadata in a JSON file to a Markdown file.
    """
    with open(json_path, 'r', encoding = "utf8") as file:
        papers_metadata = json.load(file)
    dict_to_md(papers_metadata)


def main():
    keywords = ["Physics", "Diffusion", "Finance"]
    max_results = [8, 8, 3]
    papers = {}
    for i, keyword in enumerate(keywords):
        papers_per_keyword = search_by_keyword(keyword, max_results[i])
        papers[keyword] = papers_per_keyword
    papers_metadata = save_to_json(papers)
    dict_to_md(papers_metadata = papers_metadata)


if __name__ == "__main__":
    main()
