# from xhtml2pdf import pisa
# import cStringIO as StringIO
# from django.template.loader import get_template
# from django.template import Context
import sys # This will help me get the arguments passed from the command line


# def html_to_pdf_directly(request):
# 	template = get_template("template_name.html")
# 	context = Context({'pagesize':'A4'})
# 	html = template.render(context)
# 	result = StringIO.StringIO()
# 	pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result)
# 	if not pdf.err:
# 		return HttpResponse(result.getvalue(), content_type='application/pdf')
# 	else: return HttpResponse('Errors')


def main():
	print("Hello from main")
	print("My argument at 1 is %s" % (sys.argv[1]))


if __name__ == "__main__":
	main()
