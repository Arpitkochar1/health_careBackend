from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializer for User data (used in registration response)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        # PostgreSQL: User data is stored in the 'auth_user' table (Django's default User model).
        # JWT: This serializer formats user data returned after registration or login.

# Serializer for User Registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # PostgreSQL: When a user is created, Django ORM saves it to the 'auth_user' table in PostgreSQL.
        # JWT: The view using this serializer (RegisterView) generates JWT tokens after user creation.

    def create(self, validated_data):
        # Creates a user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
        # PostgreSQL: The create_user method saves the user to the PostgreSQL database.
        # JWT: The view (in views.py) uses simplejwt to generate access/refresh tokens after this.

# Serializer for Patient model
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_by',)
        # PostgreSQL: Patient data is stored in the 'api_patient' table (based on the Patient model).
        # JWT: Only authenticated users (verified via JWT token) can create patients, and 'created_by' is set to the authenticated user.

    def validate_email(self, value):
        # Example validation for email
        if '@' not in value:
            raise serializers.ValidationError("Invalid email format.")
        return value
        # PostgreSQL: Validation ensures data integrity before saving to the database.
        # JWT: No direct JWT interaction here, but the view ensures the request is authenticated.

# Serializer for Doctor model
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        # PostgreSQL: Doctor data is stored in the 'api_doctor' table.
        # JWT: Only authenticated users (via JWT) can create or access doctor data.

# Serializer for PatientDoctorMapping model
class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        # PostgreSQL: Mapping data is stored in the 'api_patientdoctormapping' table.
        # JWT: Only authenticated users can create mappings, enforced by the view.

    def validate(self, data):
        # Ensure patient and doctor exist and are valid
        if not Patient.objects.filter(id=data['patient'].id).exists():
            raise serializers.ValidationError("Patient does not exist.")
        if not Doctor.objects.filter(id=data['doctor'].id).exists():
            raise serializers.ValidationError("Doctor does not exist.")
        return data
        # PostgreSQL: Validation checks ensure foreign keys (patient, doctor) exist in the database.
        # JWT: No direct JWT interaction, but the view ensures authentication.