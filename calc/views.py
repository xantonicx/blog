from django.shortcuts import render, redirect
import math
from decimal import Decimal, InvalidOperation

from django.http import HttpResponseRedirect
from math import radians, sin, cos, tan, asin, acos, atan, degrees, pi
import random
import string

from .models import TodoItem
from .forms import TodoItemForm

def todo_view(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoItemForm()

    todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'form': form, 'todo_items': todo_items})

def toggle_todo(request, todo_id):
    todo_item = TodoItem.objects.get(id=todo_id)
    todo_item.completed = not todo_item.completed
    todo_item.save()
    return redirect('todo')




def clock_view(request):
    return render(request, 'clock.html')

def stopwatch_view(request):
    return render(request, 'stopwatch.html')

def generate_password(request):
    password = None
    if request.method == 'POST':
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(16))
    return render(request, 'generator.html', {'password': password})

def trig_calculator(request):
    context = {}
    if request.method == 'POST':
        angle_degrees = request.POST.get('angle')
        angle_radians = radians(float(angle_degrees))
        sin_value = sin(angle_radians)
        cos_value = cos(angle_radians)
        tan_value = tan(angle_radians)
        # Calculate cosecant, secant, and cotangent, handling division by zero
        csc_value = 1 / sin_value if sin_value else 'undefined'
        sec_value = 1 / cos_value if cos_value else 'undefined'
        cot_value = 1 / tan_value if tan_value else 'undefined'


        # Ensure the values are in the domain of the inverse functions
        if -1 <= sin_value <= 1:
            arcsin_value = degrees(asin(sin_value))
        else:
            arcsin_value = 'undefined'
        if -1 <= cos_value <= 1:
            arccos_value = degrees(acos(cos_value))
        else:
            arccos_value = 'undefined'
        # Since atan is defined for all real numbers, no need to check
        arctan_value = degrees(atan(tan_value))
        
        context = {
            'angle_degrees': angle_degrees,
            'angle_radians': angle_radians,
            'sin_value': sin_value,
            'cos_value': cos_value,
            'tan_value': tan_value,
            'csc_value': csc_value,
            'sec_value': sec_value,
            'cot_value': cot_value,


            'arcsin_value': arcsin_value,
            'arccos_value': arccos_value,
            'arctan_value': arctan_value
        }
    return render(request, 'trig.html', context)


def carousel_b(request):
    return render(request, 'carousellite/carousel-b.html')

def carousel_256(request):
    return render(request, 'carousellite/carousel-256.html')

def carousel_128(request):
    return render(request, 'carousellite/carousel-128.html')

def carousel_64(request):
    return render(request, 'carousellite/carousel-64.html')

def carousel_32(request):
    return render(request, 'carousellite/carousel-32.html')

def carousel_16(request):
    return render(request, 'carousellite/carousel-16.html')

def carousel_8(request):
    return render(request, 'carousellite/carousel-8.html')

def carousel_lite(request):
    return render(request, 'carousellite/carousel-lite.html')

def blank_index(request):
    #categories = Category.objects.all()
    return render(request, 'blank_index.html', {"blank_index":blank_index})

def calculator(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1', 0)
        try:
            num1 = Decimal(num1)
        except InvalidOperation:
            # Handle invalid input for num1
            pass

        num2 = request.POST.get('num2', 0)
        try:
            num2 = Decimal(num2)
        except InvalidOperation:
            # Handle invalid input for num2
            pass

        operation = request.POST.get('operation')


        if operation == 'add':
            result7 = num1 + num2, ("="), (num1), ("+"), (num2)

        elif operation == 'subtract':
            result7 = num1 - num2, ("="), (num1), ("-"), (num2)

        elif operation == 'multiply':
            result7 = num1 * num2, ("="), (num1), ("x"), (num2)

        elif operation == 'divide':
            if num2 != 0:
                result7 = num1 / num2, ("="), (num1), ("/"), (num2)
            else:
                result7 = "Error: Division by zero"

        elif operation == 'sqrt':
            result7 = math.sqrt(num1), ("="), (num1), ("square root")

        elif operation == 'square':
            result7 = num1 ** 2, ("="), (num1), ("squared")

        elif operation == 'reciprocal':
            if num1 != 0:
                result7 = 1 / num1, ("="), (num1), ("reciprocal")
            else:
                result7 = "Error: Division by zero"

        elif operation == 'percentage':

            if num2 != 0:
                result7 = num1 / 100, ("="), (num1),  ("percent")
            else:
                result7 = "Error: Division by zero"

        #1 Conversions 
        elif operation == 'inch_to_cm':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 * Decimal('2.54'), ("="), (num1), ("inch(es) to cm")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        elif operation == 'cm_to_inch':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 / Decimal('2.54'), ("="), (num1), ("cm to inch(es)")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        #2 Conversions 
        elif operation == 'feet_to_meter':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 * Decimal('.3048'), ("="), (num1), ("feet to meter")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        elif operation == 'meter_to_feet':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 / Decimal('.3048'), ("="), (num1), ("meter to feet")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        #3 Conversions 
        elif operation == 'mile_to_km':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 * Decimal('.621'), ("="), (num1), ("mile to km")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        elif operation == 'km_to_mile':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 / Decimal('.621'), ("="), (num1), ("km to mile")
            except InvalidOperation:
                # Handle invalid input for num1
                pass
        #4 Conversions 
        elif operation == 'inch_to_cm':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 * Decimal('2.54'), ("="), (num1), ("inch(es) to cm")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        elif operation == 'cm_to_inch':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 / Decimal('2.54'), ("="), (num1), ("cm to inch(es)")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        #5 Conversions 
        elif operation == 'feet_to_meter':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 * Decimal('.3048'), ("="), (num1), ("feet to meter")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        elif operation == 'meter_to_feet':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 / Decimal('.3048'), ("="), (num1), ("meter to feet")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        #6 Conversions 
        elif operation == 'mile_to_km':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 * Decimal('.621'), ("="), (num1), ("mile to km")
            except InvalidOperation:
                # Handle invalid input for num1
                pass

        elif operation == 'km_to_mile':
            try:
                num1 = Decimal(request.POST.get('num1', 0))
                result7 = num1 / Decimal('.621'), ("="), (num1), ("km to mile")
            except InvalidOperation:
                # Handle invalid input for num1
                pass



        else:
            result7 = "Invalid operation"

        modified_result7 = ' '.join(str(item) for item in result7)

        return render(request, 'calculator.html', {'result7': result7, 'result7': modified_result7, 'operation': operation})
    return render(request, 'calculator.html')



def picker(request):
    return render(request, 'picker/picker.html')


def color_input(request):
    if request.method == 'POST':
        # Get the hexadecimal color code from the form input
        hex_color1 = request.POST.get('hex_color1', '#FFFFFF')  # Default to white if no input provided
        border_color1 = request.POST.get('border_color1', '#FFFFFF')  # Default to white if no input provided
        hex_color2 = request.POST.get('hex_color2', '#FFFFFF')  # Default to white if no input provided
        border_color2 = request.POST.get('border_color2', '#FFFFFF')  # Default to white if no input provided
        
        r1, g1, b1 = int(hex_color1[1:3], 16), int(hex_color1[3:5], 16), int(hex_color1[5:7], 16)
        r2, g2, b2 = int(hex_color2[1:3], 16), int(hex_color2[3:5], 16), int(hex_color2[5:7], 16)

        r1b, g1b, b1b = int(border_color1[1:3], 16), int(border_color1[3:5], 16), int(border_color1[5:7], 16)
        r2b, g2b, b2b = int(border_color2[1:3], 16), int(border_color2[3:5], 16), int(border_color2[5:7], 16)
        # Calculate average components
        r_avg = (r1 + r2) // 2
        g_avg = (g1 + g2) // 2
        b_avg = (b1 + b2) // 2

        r_avg2 = (r1b + r2b) // 2
        g_avg2 = (g1b + g2b) // 2
        b_avg2 = (b1b + b2b) // 2

        # Convert back to hexadecimal
        hex_color3 = f"#{r_avg:02X}{g_avg:02X}{b_avg:02X}"
        border_color3 = f"#{r_avg2:02X}{g_avg2:02X}{b_avg2:02X}"
        #return hex_color3

        # Render the template with the specified color
        return render(request, 'colorgrid/color_grid.html', {'hex_color1': hex_color1, 'border_color1': border_color1, 'hex_color2': hex_color2, 'border_color2': border_color2, 'hex_color3': hex_color3,'border_color3': border_color3})
    else:
        # Render the initial form
        return render(request, 'colorgrid/color_input.html')


def unicode(request):
    if request.method == 'POST':
        var6 = request.POST.get('var6')
        if var6:
            try:
                var6 = int(var6)
                result6 = (chr(var6), var6)
            except ValueError:
                result6 = None
        else:
            result6 = None
    else:
        result6 = None

    if request.method == 'POST':
        var9 = request.POST.get('var9')
        if var9:
            try:
                var9 = ord(var9)
                result9 = (var9, chr(var9))
                result9a = ((var9-1), chr(var9-1), (var9-2), chr(var9-2), (var9-3), chr(var9-3), (var9-100), chr(var9-100))
                result9b = ((var9+1), chr(var9+1), chr(var9+2), chr(var9+3), chr(var9+4), chr(var9+5), 
                    chr(var9+6), chr(var9+7), chr(var9+8), chr(var9+9), chr(var9+10), chr(var9+11), chr(var9+12), chr(var9+13), chr(var9+14), 
                    chr(var9+15), chr(var9+16), chr(var9+17), chr(var9+18), chr(var9+19), chr(var9+20), chr(var9+21), chr(var9+22), chr(var9+23), chr(var9+24), 
                    chr(var9+25), chr(var9+26), chr(var9+27), chr(var9+28), chr(var9+29), chr(var9+30), chr(var9+31), chr(var9+32), chr(var9+33), chr(var9+34), 
                    chr(var9+35), chr(var9+36), chr(var9+37), chr(var9+38), chr(var9+39), chr(var9+40), chr(var9+41), chr(var9+42), chr(var9+43), chr(var9+44), 
                    chr(var9+45), chr(var9+46), chr(var9+47), chr(var9+48), chr(var9+49), chr(var9+50), chr(var9+51), chr(var9+52), chr(var9+53), chr(var9+54), 
                    chr(var9+55), chr(var9+56), chr(var9+57), chr(var9+58), chr(var9+59), chr(var9+60), chr(var9+61), chr(var9+62), chr(var9+63), chr(var9+64), 
                    chr(var9+65), chr(var9+66), chr(var9+67), chr(var9+68), chr(var9+69), chr(var9+70), chr(var9+71), chr(var9+72), chr(var9+73), chr(var9+74), 
                    chr(var9+75), chr(var9+76), chr(var9+77), chr(var9+78), chr(var9+79), chr(var9+80), chr(var9+81), chr(var9+82), chr(var9+83), chr(var9+84), 
                    chr(var9+85), chr(var9+86), chr(var9+87), chr(var9+88), chr(var9+89), chr(var9+90), chr(var9+91), chr(var9+92), chr(var9+93), chr(var9+94), 
                    chr(var9+95), chr(var9+96), chr(var9+97), chr(var9+98), chr(var9+99), (var9+100), chr(var9+101), chr(var9+102), chr(var9+103), chr(var9+104), 
                    chr(var9+105), chr(var9+106), chr(var9+107), chr(var9+108), chr(var9+109), chr(var9+110), chr(var9+111), chr(var9+112), chr(var9+113), chr(var9+114), 
                    chr(var9+115), chr(var9+116), chr(var9+117), chr(var9+118), chr(var9+119), chr(var9+120), chr(var9+121), chr(var9+122), chr(var9+123), chr(var9+124), 
                    chr(var9+125), chr(var9+126), chr(var9+127), chr(var9+128), chr(var9+129), chr(var9+130), chr(var9+131), chr(var9+132), chr(var9+133), chr(var9+134), 
                    chr(var9+135), chr(var9+136), chr(var9+137), chr(var9+138), chr(var9+139), chr(var9+140), chr(var9+141), chr(var9+142), chr(var9+143), chr(var9+144), 
                    chr(var9+145), chr(var9+146), chr(var9+147), chr(var9+148), chr(var9+149), chr(var9+150), chr(var9+151), chr(var9+152), chr(var9+153), chr(var9+154), 
                    chr(var9+155), chr(var9+156), chr(var9+157), chr(var9+158), chr(var9+159), chr(var9+160), chr(var9+161), chr(var9+162), chr(var9+163), chr(var9+164), 
                    chr(var9+165), chr(var9+166), chr(var9+167), chr(var9+168), chr(var9+169), chr(var9+170), chr(var9+171), chr(var9+172), chr(var9+173), chr(var9+174), 
                    chr(var9+175), chr(var9+176), chr(var9+177), chr(var9+178), chr(var9+179), chr(var9+180), chr(var9+181), chr(var9+182), chr(var9+183), chr(var9+184), 
                    chr(var9+185), chr(var9+186), chr(var9+187), chr(var9+188), chr(var9+189), chr(var9+190), chr(var9+191), chr(var9+192), chr(var9+193), chr(var9+194), 
                    chr(var9+195), chr(var9+196), chr(var9+197), chr(var9+198), chr(var9+199), (var9+200), chr(var9+200), chr(var9+201), chr(var9+202), chr(var9+203), chr(var9+204), 
                    chr(var9+205), chr(var9+206), chr(var9+207), chr(var9+208), chr(var9+209), chr(var9+210), chr(var9+211), chr(var9+212), chr(var9+213), chr(var9+214), 
                    chr(var9+215), chr(var9+216), chr(var9+217), chr(var9+218), chr(var9+219), chr(var9+220), chr(var9+221), chr(var9+222), chr(var9+223), chr(var9+224), 
                    chr(var9+225), chr(var9+226), chr(var9+227), chr(var9+228), chr(var9+229), chr(var9+230), chr(var9+231), chr(var9+232), chr(var9+233), chr(var9+234), 
                    chr(var9+235), chr(var9+236), chr(var9+237), chr(var9+238), chr(var9+239), chr(var9+240), chr(var9+241), chr(var9+242), chr(var9+243), chr(var9+244), 
                    chr(var9+245), chr(var9+246), chr(var9+247), chr(var9+248), chr(var9+249), chr(var9+250), chr(var9+251), chr(var9+252), chr(var9+253), chr(var9+254), 
                    chr(var9+255), chr(var9+256), chr(var9+257), chr(var9+258), chr(var9+259), chr(var9+260), chr(var9+261), chr(var9+262), chr(var9+263), chr(var9+264), 
                    chr(var9+265), chr(var9+266), chr(var9+267), chr(var9+268), chr(var9+269), chr(var9+270), chr(var9+271), chr(var9+272), chr(var9+273), chr(var9+274), 
                    chr(var9+275), chr(var9+276), chr(var9+277), chr(var9+278), chr(var9+279), chr(var9+280), chr(var9+281), chr(var9+282), chr(var9+283), chr(var9+284), 
                    chr(var9+285), chr(var9+286), chr(var9+287), chr(var9+288), chr(var9+289), chr(var9+290), chr(var9+291), chr(var9+292), chr(var9+293), chr(var9+294), 
                    chr(var9+295), chr(var9+296), chr(var9+297), chr(var9+298), chr(var9+299), (var9+300), chr(var9+300), chr(var9+301), chr(var9+302), chr(var9+303), chr(var9+304), 
                    chr(var9+305), chr(var9+306), chr(var9+307), chr(var9+308), chr(var9+309), chr(var9+310), chr(var9+311), chr(var9+312), chr(var9+313), chr(var9+314), 
                    chr(var9+315), chr(var9+316), chr(var9+317), chr(var9+318), chr(var9+319), chr(var9+320), chr(var9+321), chr(var9+322), chr(var9+323), chr(var9+324), 
                    chr(var9+325), chr(var9+326), chr(var9+327), chr(var9+328), chr(var9+329), chr(var9+330), chr(var9+331), chr(var9+332), chr(var9+333), chr(var9+334), 
                    chr(var9+335), chr(var9+336), chr(var9+337), chr(var9+338), chr(var9+339), chr(var9+340), chr(var9+341), chr(var9+342), chr(var9+343), chr(var9+344), 
                    chr(var9+345), chr(var9+346), chr(var9+347), chr(var9+348), chr(var9+349), chr(var9+350), chr(var9+351), chr(var9+352), chr(var9+353), chr(var9+354), 
                    chr(var9+355), chr(var9+356), chr(var9+357), chr(var9+358), chr(var9+359), chr(var9+360), chr(var9+361), chr(var9+362), chr(var9+363), chr(var9+364), 
                    chr(var9+365), chr(var9+366), chr(var9+367), chr(var9+368), chr(var9+369), chr(var9+370), chr(var9+371), chr(var9+372), chr(var9+373), chr(var9+374), 
                    chr(var9+375), chr(var9+376), chr(var9+377), chr(var9+378), chr(var9+379), chr(var9+380), chr(var9+381), chr(var9+382), chr(var9+383), chr(var9+384), 
                    chr(var9+385), chr(var9+386), chr(var9+387), chr(var9+388), chr(var9+389), chr(var9+390), chr(var9+391), chr(var9+392), chr(var9+393), chr(var9+394), 
                    chr(var9+395), chr(var9+396), chr(var9+397), chr(var9+398), chr(var9+399), (var9+400), chr(var9+400), chr(var9+401), chr(var9+402), chr(var9+403), chr(var9+404), 
                    chr(var9+405), chr(var9+406), chr(var9+407), chr(var9+408), chr(var9+409), chr(var9+410), chr(var9+411), chr(var9+412), chr(var9+413), chr(var9+414), 
                    chr(var9+415), chr(var9+416), chr(var9+417), chr(var9+418), chr(var9+419), chr(var9+420), chr(var9+421), chr(var9+422), chr(var9+423), chr(var9+424), 
                    chr(var9+425), chr(var9+426), chr(var9+427), chr(var9+428), chr(var9+429), chr(var9+430), chr(var9+431), chr(var9+432), chr(var9+433), chr(var9+434), 
                    chr(var9+435), chr(var9+436), chr(var9+437), chr(var9+438), chr(var9+439), chr(var9+440), chr(var9+441), chr(var9+442), chr(var9+443), chr(var9+444), 
                    chr(var9+445), chr(var9+446), chr(var9+447), chr(var9+448), chr(var9+449), chr(var9+450), chr(var9+451), chr(var9+452), chr(var9+453), chr(var9+454), 
                    chr(var9+455), chr(var9+456), chr(var9+457), chr(var9+458), chr(var9+459), chr(var9+460), chr(var9+461), chr(var9+462), chr(var9+463), chr(var9+464), 
                    chr(var9+465), chr(var9+466), chr(var9+467), chr(var9+468), chr(var9+469), chr(var9+470), chr(var9+471), chr(var9+472), chr(var9+473), chr(var9+474), 
                    chr(var9+475), chr(var9+476), chr(var9+477), chr(var9+478), chr(var9+479), chr(var9+480), chr(var9+481), chr(var9+482), chr(var9+483), chr(var9+484), 
                    chr(var9+485), chr(var9+486), chr(var9+487), chr(var9+488), chr(var9+489), chr(var9+490), chr(var9+491), chr(var9+492), chr(var9+493), chr(var9+494), 
                    chr(var9+495), chr(var9+496), chr(var9+497), chr(var9+498), chr(var9+499), (var9+500), chr(var9+500))
                modified_result9b = ' '.join(str(item) for item in result9b)
                
                modified_result9a = ' '.join(str(item) for item in result9a)


            except ValueError:
                result9 = None
                result9a = None
                result9b = None
                modified_result9a = None
                modified_result9b = None
        else:
            result9 = None
            result9a = None
            result9b = None
            modified_result9a = None
            modified_result9b = None
    else:
        result9 = None
        result9a = None
        result9b = None
        modified_result9a = None
        modified_result9b = None

    return render(request, 'unicode.html', {'result9': result9, 'result6': result6, 'result9a': modified_result9a, 'result9b': modified_result9b})

def yt_000001(request):
    return render(request, 'youtube/yt_000001.html')


def blank5(request):
    return render(request, 'blank/blank5.html')

def blank6(request):
    return render(request, 'blank/blank6.html')

def blank7(request):
    return render(request, 'blank/blank7.html')

def blank8(request):
    return render(request, 'blank/blank8.html')
 
def blank9(request):
    return render(request, 'blank/blank9.html')

def blank10(request):
    return render(request, 'blank/blank10.html')

def blank11(request):
    return render(request, 'blank/blank11.html')

def blank12(request):
    return render(request, 'blank/blank12.html')

def blank13(request):
    return render(request, 'blank/blank13.html')

def blank14(request):
    return render(request, 'blank/blank14.html')

def blank15(request):
    return render(request, 'blank/blank15.html')


def album(request):
    return render(request, 'bootstrap/album/album.html')
def album_rtl(request):
    return render(request, 'bootstrap/album-rtl/album-rtl.html')
def badges(request):
    return render(request, 'bootstrap/badges/badges.html')
def blog(request):
    return render(request, 'bootstrap/blog/blog.html')
def blog_rtl(request):
    return render(request, 'bootstrap/blog-rtl/blog-rtl.html')
def breadcrumbs(request):
    return render(request, 'bootstrap/breadcrumbs/breadcrumbs.html')
def buttons(request):
    return render(request, 'bootstrap/buttons/buttons.html')
def carousel(request):
    return render(request, 'bootstrap/carousel/carousel.html')
def carousel_rtl(request):
    return render(request, 'bootstrap/carousel-rtl/carousel-rtl.html')
def cheatsheet(request):
    return render(request, 'bootstrap/cheatsheet/cheatsheet.html')
def cheatsheet_rtl(request):
    return render(request, 'bootstrap/cheatsheet-rtl/cheatsheet-rtl.html')
def checkout(request):
    return render(request, 'bootstrap/checkout/checkout.html')
def checkout_rtl(request):
    return render(request, 'bootstrap/checkout-rtl/checkout-rtl.html')
def cover(request):
    return render(request, 'bootstrap/cover/cover.html')
def dashboard(request):
    return render(request, 'bootstrap/dashboard/dashboard.html')
def dashboard_rtl(request):
    return render(request, 'bootstrap/dashboard-rtl/dashboard-rtl.html')
def dropdowns(request):
    return render(request, 'bootstrap/dropdowns/dropdowns.html')
def features(request):
    return render(request, 'bootstrap/features/features.html')
def footers(request):
    return render(request, 'bootstrap/footers/footers.html')
def grid(request):
    return render(request, 'bootstrap/grid/grid.html')
def headers(request):
    return render(request, 'bootstrap/headers/headers.html')
def heroes(request):
    return render(request, 'bootstrap/heroes/heroes.html')
def jumbotron(request):
    return render(request, 'bootstrap/jumbotron/jumbotron.html')
def jumbotrons(request):
    return render(request, 'bootstrap/jumbotrons/jumbotrons.html')
def list_groups(request):
    return render(request, 'bootstrap/list-groups/list-groups.html')
def masonry(request):
    return render(request, 'bootstrap/masonry/masonry.html')
def modals(request):
    return render(request, 'bootstrap/modals/modals.html')
def navbar_bottom(request):
    return render(request, 'bootstrap/navbar-bottom/navbar-bottom.html')
def navbar_fixed(request):
    return render(request, 'bootstrap/navbar-fixed/navbar-fixed.html')
def navbars(request):
    return render(request, 'bootstrap/navbars/navbars.html')
def navbars_offcanvas(request):
    return render(request, 'bootstrap/navbars-offcanvas/navbars-offcanvas.html')
def navbar_static(request):
    return render(request, 'bootstrap/navbar-static/navbar-static.html')
def offcanvas(request):
    return render(request, 'bootstrap/offcanvas/offcanvas.html')
def offcanvas_navbar(request):
    return render(request, 'bootstrap/offcanvas-navbar/offcanvas-navbar.html')
def pricing(request):
    return render(request, 'bootstrap/pricing/pricing.html')
def product(request):
    return render(request, 'bootstrap/product/product.html')
def sidebars(request):
    return render(request, 'bootstrap/sidebars/sidebars.html')
def sign_in(request):
    return render(request, 'bootstrap/sign-in/sign-in.html')
def starter_template(request):
    return render(request, 'bootstrap/starter-template/starter-template.html')
def sticky_footer(request):
    return render(request, 'bootstrap/sticky-footer/sticky-footer.html')
def sticky_footer_navbar(request):
    return render(request, 'bootstrap/sticky-footer-navbar/sticky-footer-navbar.html')





