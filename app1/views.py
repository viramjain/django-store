from django.shortcuts import render,redirect
from .models import Product,Orders
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def CartItems(cart):
    items=[]
    for item in cart:
        items.append(Product.objects.get(id=item))
    return items


def Home(req):
    if 'cart' not in req.session:
        req.session['cart']=[]
    cart=req.session['cart']
    req.session.set_expiry(0)
    store_items=Product.objects.all()
    context={
        'items':store_items,'cart_size':len(cart)
    }
    if req.method=='POST':
        cart.append(int(req.POST['obj_id']))
        return redirect('/')
    return render(req,'app1/home.html',context)
def Cart(req):
    cart=req.session['cart']
    req.session.set_expiry(0)
    context={
        'cart':cart,'cart_size':len(cart),'cart_items':CartItems(cart),'total_price':priceCart(cart)}
    return render(req,'app1/cart.html',context)
def genItemList(cart):
    cart_items=CartItems(cart)
    item_list=""
    for item in cart_items:
        item_list+=str(item.product_name)
        item_list+=','
    return item_list


def priceCart(cart):
    cart_items=CartItems(cart)
    price=0
    for item in cart_items:
        price+=item.product_price
    return price
def removeFromCart(req):
    req.session.set_expiry(0)
    obj_to_remove=int(req.POST['obj_id'])
    obj_index=req.session['cart'].index(obj_to_remove)
    req.session['cart'].pop(obj_index)
    return redirect('cart')
def checkout(req):
    req.session.set_expiry(0)
    cart=req.session['cart']
    context={
        'cart':cart,'cart_size':len(cart),'total_price':priceCart(cart)}
    return render(req,'app1/checkout.html',context)
def completeOrders(req):
    req.session.set_expiry(0)
    cart=req.session['cart']
    order=Orders()
    order.first_name=req.POST['first_name']
    order.last_name=req.POST['last_name']
    order.city=req.POST['city']
    order.address=req.POST['address']
    order.payment_method=req.POST['payment']
    order.payment_date=req.POST['payment_data']
    order.items=genItemList(cart)
    order.save()
    req.session['cart']=[]
    return render(req,'app1/complete_order.html',None)

def adminLogin(req):
    if req.method=="POST":
        username=req.POST['username']
        password=req.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('admin')
        else:
            return render(req,"admin_login",{'login':False})
    return render(req,"app1/admin_login.html",None)
@login_required
def adminDashboard(req):
    orders=Orders.objects.all()
    context={'orders':orders}
    return render(req,'app1/admin_panel.html',context)

