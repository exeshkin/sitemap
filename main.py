import json

xml_text = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
	<url>
		<loc>https://uliyanovsk.ru/</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/minister-sklonnyi.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/minister-akatov.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/minister-serobyan.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/minister-ivanov.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/event-article.html</loc>
	</url>
    <url>
		<loc>https://uliyanovsk.ru/message-years-1947-1957.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/message-years-1958-1962.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/message-years-1963-1965.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/testimony.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/worship.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/psalms-2022.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/psalms-2021.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/psalms-2020.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/gallery-list.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/video-list.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/stream.html</loc>
	</url>
	<url>
		<loc>https://uliyanovsk.ru/contacts.html</loc>
	</url>
'''

xml_text_finish = '</urlset>\n'


def create_sitemap_xml(xml_text, xml_text_finish):
    with open('data.json', 'r', encoding='utf-8') as file_data:
        file_json = json.load(file_data)

        len_services = 0
        len_message = 0
        len_video = 0
        len_photo = 0

        for service in file_json['services']:
            len_services = len(file_json['services'])
            elem = f'    <url>\n        <loc>https://uliyanovsk.ru/event-article.html?id={service}</loc>\n    </url>\n'
            xml_text += elem

        for sermon in file_json['message']:
            len_message = len(file_json['message'])
            elem = f'    <url>\n        <loc>https://uliyanovsk.ru/message-article.html?id={sermon}</loc>\n    </url>\n'
            xml_text += elem

        for video in file_json['gallery']:
            if file_json['gallery'][video]['category'] == 'Видеообзор':
                len_video += 1
                elem = f'    <url>\n        <loc>https://uliyanovsk.ru/video-article.html?id={video}</loc>\n    </url>\n'
                xml_text += elem

        for photo in file_json['gallery']:
            if file_json['gallery'][photo]['category'] == 'Видеообзор':
                len_photo += 1
                elem = f'    <url>\n        <loc>https://uliyanovsk.ru/photo-article.html?id={photo}</loc>\n    </url>\n'
                xml_text += elem

        xml_text += xml_text_finish

        with open('sitemap.xml', 'w', encoding='utf-8') as file_xml:
            file_xml.write(xml_text)

        print('В файл sitemap.xml добавлены:')
        print(f'{len_services} местных служений')
        print(f'{len_message} служений Послания')
        print(f'{len_video} видеообзоров')
        print(f'{len_photo} фотообзоров')


def main():
    create_sitemap_xml(xml_text, xml_text_finish)


if __name__ == '__main__':
    main()
