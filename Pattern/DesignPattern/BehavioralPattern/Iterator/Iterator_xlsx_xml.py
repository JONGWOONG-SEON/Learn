import zipfile
import xml.etree.ElementTree as ET
import shutil
import os

xlsx_file = "/Users/sun/Desktop/Mirror/TIL/Pattern/DesignPattern/BehavioralPattern/Iterator/TestFolder/test.xlsx"
zip_file = "/Users/sun/Desktop/Mirror/TIL/Pattern/DesignPattern/BehavioralPattern/Iterator/TestFolder/convert.zip"
extract_dir = "/Users/sun/Desktop/Mirror/TIL/Pattern/DesignPattern/BehavioralPattern/Iterator/TestFolder/"

# XLSX를 ZIP으로 변환 후 압축 해제
shutil.copy(xlsx_file, zip_file)
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# sheet1.xml에서 12자리 이상의 숫자를 문자열로 변환
sheet_path = f"{extract_dir}/xl/worksheets/sheet1.xml"
tree = ET.parse(sheet_path)
root = tree.getroot()

ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
ET.register_namespace('', ns['main'])

shared_strings_path = f"{extract_dir}/xl/sharedStrings.xml"
if os.path.exists(shared_strings_path):
    sst_tree = ET.parse(shared_strings_path)
    sst_root = sst_tree.getroot()
else:
    sst_root = ET.Element("sst", xmlns=ns['main'])

def add_shared_string(value):
    si = ET.Element("si")
    t = ET.SubElement(si, "t")
    t.text = str(value)
    sst_root.append(si)
    print(t.text)
    return len(sst_root) - 1

# 변환 작업
for cell in root.findall(".//main:c", ns):
    value_element = cell.find("main:v", ns)
    if value_element is not None:
        try:
            float_value = float(value_element.text)
            if float_value >= 1e12:  # 12자리 이상이면 변환
                new_index = add_shared_string(value_element.text)
                cell.set("t", "s")
                value_element.text = str(new_index)
        except ValueError:
            pass

# XML 저장
tree.write(sheet_path, encoding="utf-8", xml_declaration=True)
sst_tree = ET.ElementTree(sst_root)
sst_tree.write(shared_strings_path, encoding="utf-8", xml_declaration=True)



# 다시 ZIP으로 압축
output_xlsx = "modified.xlsx"
shutil.make_archive("modified", 'zip', extract_dir)
os.rename("modified.zip", output_xlsx)

# 정리
# shutil.rmtree(extract_dir)
# os.remove(zip_file)

print(f"변환 완료: {output_xlsx}")
