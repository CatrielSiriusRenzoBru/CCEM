from django.shortcuts import render,HttpResponse,redirect
from django.utils.six import BytesIO
import qrcode
from django.db import connection

# Create your views here.

def index(request):
    return HttpResponse('ok')


def generate_qrcode(request):
    data = 'www.brisasoluciones.com'
    img = qrcode.make(data)

    buf = BytesIO()		# BytesIO se da cuenta de leer y escribir bytes en la memoria
    img.save(buf)
    image_stream = buf.getvalue()

    return render(request, 'Planilla/qr.html',
                  {'image_stream': image_stream})

def form_add (request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            propietario =request.POST['propietario']
            mz = request.POST['mz']
            lt = request.POST['lt']
            Usuario = request.POST['Usuario']
            cant = request.POST['cant']
            with connection.cursor() as cursor:
                dia = 'select NOW()'
                cursor.execute(dia)
                dia = cursor.fetchone()
            reserva = 'INSERT INTO `planilla_planilla`( `Dia`, `Propietario`, `Manzana`, `Lote`, `Usuario`, `cant`, `Aprobado`) VALUES(\'%s\',\'%s\',%s,%s,\'%s\',%s,0)'%(dia[0],propietario,mz,lt,Usuario,cant)
            with connection.cursor() as cursor:
                print(reserva)
                cursor.execute(reserva)
                return redirect('/')
        return render(request, "Planilla/add.html")
         #otro caso redireccionamos al login
    return redirect('/login')

def list (request):
    return render(request, "Planilla/list.html")