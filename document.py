from docxtpl import DocxTemplate


doc = DocxTemplate("invoice.docx")

invoice_list = [[2, "pen", 0.5, 1]]

doc.render({"name" :"John", "invoice_list" : invoice_list})
doc.save("newInvoice.docx")