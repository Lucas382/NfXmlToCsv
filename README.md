# XmlToCsv Project Overview


#### This solution was developed in Python using the [Flet](https://flet.dev/) framework to handle <br> the needs of a  freelancer job which required a solution to convert XML files to CSV.

---

- My initial goal for this project was to develop a reusable project template, so the components could be used again.

![1_first_entry](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/5144d0f2-6e97-43c6-9ed6-2bf57fd2e60f)

---
- The project includes a directory selector, which allows users to choose the appropriate folder containing the xml files.
  
![2_xml_folder_selector_dialog](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/50c2e156-264d-4be5-92d4-315430a25496)

---
- It remembers the last folder that the user inputted to facilitate the next conversion.

![3 1_xml_folder_selected](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/c78ad883-03a0-4f3f-859b-3b734388125c)

> Saved path on a Json file.

![3 2_saved_dir_path](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/23d84f73-3e47-4919-b12f-32ca2471305f)

---
-  It features a save system that allows the user to choose where to save the CSV file.

![4_save_xlsx_file_dialog](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/d2bb38c3-9392-4765-8b01-58dc9555dc8b)

---
- It also has an information console to track the current status of the conversion process.
>Note: A 1-second delay was applied to simulate the processing of hundreds of XML files.

![5_conversion_started](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/1d977020-cdf6-4cbf-8858-88ba33220639)

>Example of a successful conversion.

![6_success_conversion](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/54a1b2cc-1b38-447a-8b02-439faa75c52a)

>Example of a failed conversion with the reason being no XML file in the selected folder.

![7_error_no_xml_file](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/1bbdf680-4c33-47b0-882e-d20138dab69c)

>Example of a failed conversion with the reason being no XML directory specified.

![8_error_no_xml_folder](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/e731972c-d098-4a6f-bddd-d44d8b805153)

>Resulting CSV file as requested by the client.

![result](https://github.com/Lucas382/NfXmlToCsv/assets/44009909/35dea528-674e-49d6-b340-1965b52bebb2)
<p align='right'>Fake data</p>

---



