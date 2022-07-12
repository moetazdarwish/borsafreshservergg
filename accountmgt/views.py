
from django.db.models import Q, Sum
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from accountmgt.accountserializer import ExpenseAccountSerializer, CashOutAccountSerializer
from accountmgt.models import ExpensesAccount, CashOutAccount
from profils.models import UsersProfiles
# Create your views here.



######user



#####suplier



@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiAccountAll(request):
    language = request.headers['Accept-language']
    items = UsersProfiles.objects.get(name=request.user)
    total = ExpensesAccount.objects.filter(supplier=items).aggregate(expense=Sum('expense'))['expense']
    get_box = ExpensesAccount.objects.filter(supplier=items)
    ser_list = {}
    if total:
        ser_list = ExpenseAccountSerializer(instance=get_box, many=True,context={'lang': language}).data
    return Response(ser_list)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def apiAccountPayment(request):
    language = request.headers['Accept-language']
    items = UsersProfiles.objects.get(name=request.user)
    total = CashOutAccount.objects.filter(supplier=items).aggregate(expense=Sum('expense'))['expense']
    get_box = CashOutAccount.objects.filter(supplier=items)
    ser_list = {}
    if total:
        ser_list = CashOutAccountSerializer(instance=get_box, many=True,context={'lang': language}).data
    return Response(ser_list)

