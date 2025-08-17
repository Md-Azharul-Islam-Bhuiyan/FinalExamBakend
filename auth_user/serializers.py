from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ShopUserAccount, UserAddress
from .constants import GENDER_TYPE


class ShopUserAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShopUserAccount
        fields = '__all__'

class UserAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'

class ShopUserRegistrationSerializers(serializers.ModelSerializer):
    phone_no = serializers.CharField(required=True)
    birth_date = serializers.DateField(input_formats=['%Y-%m-%d'], write_only=True)
    gender = serializers.ChoiceField(choices=GENDER_TYPE)
    profile_picture = serializers.ImageField()
    street_address = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    postal_code = serializers.IntegerField()
    country = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_no', 'birth_date', 'gender', 'profile_picture', 'street_address', 'city', 'postal_code', 'country','password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        phone_no = self.validated_data['phone_no']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        birth_date = self.validated_data['birth_date']
        gender = self.validated_data['gender']
        profile_picture = self.validated_data['profile_picture']
        street_address = self.validated_data['street_address']
        city = self.validated_data['city']
        postal_code = self.validated_data['postal_code']
        country = self.validated_data['country']
        



        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Matched"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        

        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()

        ShopUserAccount.objects.create(
            user = account, 
            birth_date = birth_date,
            gender = gender,
            profile_picture = profile_picture,
            phone_no = phone_no,
            account_no = 1000+account.id
        )

        UserAddress.objects.create(
                user = account,
                postal_code = postal_code,
                city = city,
                country = country,
                street_address = street_address
            )
        return account
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)