# Article Metadata Field Guide

Open `articles.csv` in Excel or Google Sheets. One row = one article.
Add or delete rows as needed — the placeholder rows just pre-fill the volume/issue/year for you.

## Column Descriptions

| Column | Example | Notes |
|---|---|---|
| `volume` | `1` | Integer |
| `issue` | `1` | Integer |
| `year` | `2024` | 4-digit year |
| `article_title` | `A Study of X` | Full title as it appears in the PDF |
| `authors` | `Jane Smith \| John Doe` | Separate multiple authors with ` \| ` |
| `affiliations` | `MIT \| Yale` | One per author, same order, separated by ` \| ` |
| `abstract` | `This paper examines...` | Full abstract text |
| `keywords` | `machine learning, NLP` | Comma-separated list |
| `page_start` | `1` | First page of the article inside the issue PDF |
| `page_end` | `12` | Last page of the article inside the issue PDF |
| `doi` | `10.XXXXX/ijscar.v1i1.001` | Leave blank if not yet assigned |
| `notes` | `open access` | Optional: invited paper, erratum, etc. |

## Tips

- If an author has no listed affiliation, leave that position blank but keep the pipe separators so the count stays aligned with authors — e.g. `MIT | | Harvard`.
- Abstracts can contain commas freely; just make sure the cell stays as a single cell in your spreadsheet (don't break it across columns).
- Page numbers refer to pages *within the PDF file*, not the printed page numbers on the paper if they differ.
