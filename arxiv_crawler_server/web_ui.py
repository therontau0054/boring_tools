import os
import json
import streamlit as st

metadata_dir = "./papers_metadata"


@st.cache_data(ttl = 600)
def get_updated_date():
    files = os.listdir(metadata_dir)
    files = sorted(files, key = lambda file: os.path.getctime(os.path.join(metadata_dir, file)), reverse = True)
    date = list(map(lambda x: x.split('_')[1].split('.')[0], files))
    date = list(map(lambda x: f"20{x[:2]}-{x[2:4]}-{x[4:]}", date))
    return date


def display_papers():
    st.set_page_config(layout = "wide")
    dates = get_updated_date()
    if len(dates) == 0:
        st.write("No papers metadata available.")
        return

    def write_data(date):
        st.title("Papers' Metadata 📄")
        st.header(f"Updated on {date}")
        date = date.replace("-", "")[2:]
        file_path = f"{metadata_dir}/papers_{date}.json"
        with open(file_path, 'r', encoding = "utf8") as f:
            papers_metadata = json.load(f)

        abstracts_content = "<div style='text-align: justify'>\n\n"
        for k, v in papers_metadata.items():
            st.subheader(k)
            abstracts_content += f"## {k}\n"
            table_content = "|Publish Date|Updated Date|Title|Authors|PDF|\n"
            table_content += "|---|---|---|---|---|\n"
            for p in v:
                published_date = p["published"].split()[0]
                updated_date = p["updated"].split()[0]
                title = p["title"]
                authors = p["authors"].split(", ")[0]
                pdf_url = p["pdf_url"]
                pdf_id = pdf_url.split('/')[-1]

                abstract = p["summary"]
                abstracts_content += f"### {title}\n\n"
                abstracts_content += f"**Authors**: {p['authors']}\n\n"
                abstracts_content += f"**Published Date**: {published_date}\n\n"
                abstracts_content += f"**Updated Date**: {updated_date}\n\n"
                abstracts_content += f"**PDF Url**: [{pdf_id}]({pdf_url})\n\n"
                abstracts_content += f"**Abstract**: {abstract}\n\n\n"

                table_content += f"|{published_date}"
                table_content += f"|{updated_date}"
                table_content += f"|{title}"
                table_content += f"|{authors.split(', ')[0]}"
                table_content += f"|[{pdf_id}]({pdf_url})|\n"
            st.markdown(table_content)
        abstracts_content += "</div>\n\n"
        st.title("Abstracts")
        st.markdown(abstracts_content, unsafe_allow_html = True)

    selected_date = None
    for date_str in dates:
        if st.sidebar.button(date_str):
            selected_date = date_str
    if selected_date:
        write_data(selected_date)
    else:
        write_data(dates[0])


display_papers()
# streamlit run .\web_ui.py
