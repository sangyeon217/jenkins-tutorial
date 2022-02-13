from py.xml import html
from py.xml import raw
from etc import file_func


def create(html_file, html_title):
    # CSS 파일 텍스트로 변환
    css_file = 'file/html/assets/style.css'
    css_text = file_func.convert_file_to_text(file=css_file)

    # HTML head 입력
    html_head = html.head(
        html.meta(charset="utf-8"),
        html.meta(name="viewport", content="width=device-width,initial-scale=1.0"),
        html.title(html_title),
        html.style(raw(css_text))
    )

    # HTML body 입력
    html_body = html.body(
        html.h1("Results"),
        html.p("GitHub 링크"),
        raw(rtn_a_tag(url="https://github.com/sangyeon217/jenkins-tutorial", content='https://github.com/sangyeon217/jenkins-tutorial'))
    )

    doc = html.html(html_head, html_body)
    doc.unicode(indent=2).encode('utf8')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(doc))


def rtn_a_tag(url, content):
    a_tag_text = '<a href=' + url + ' target="_blank">' + content + '</a>'
    return a_tag_text
