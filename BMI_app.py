def calculate_bmi(weight_kg, height_m):
    """حساب مؤشر كتلة الجسم"""
    bmi = weight_kg / (height_m ** 2)
    return bmi


def get_bmi_category(bmi):
    """تحديد فئة الوزن بناءً على مؤشر كتلة الجسم"""
    if bmi < 18.5:
        return "نقص في الوزن"
    elif 18.5 <= bmi < 25:
        return "وزن طبيعي"
    elif 25 <= bmi < 30:
        return "زيادة في الوزن"
    else:
        return "سمنة"


# عرض معلومات البرنامج
print("=" * 40)
print("📊 حاسبة مؤشر كتلة الجسم (BMI)")
print("=" * 40)

# الحصول على المدخلات من المستخدم
try:
    weight = float(input("أدخل وزنك بالكيلوغرام: "))
    height = float(input("أدخل طولك بالأمتار (مثال: 1.75): "))

    # التحقق من صحة المدخلات
    if weight <= 0 or height <= 0:
        print("❌ خطأ: يجب أن يكون الوزن والطول أكبر من صفر!")
    else:
        # حساب BMI
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        # عرض النتيجة
        print("\n" + "=" * 40)
        print(f"📋 النتيجة:")
        print(f"   مؤشر كتلة الجسم: {bmi:.2f}")
        print(f"   الفئة: {category}")
        print("=" * 40)

        # جدول المرجعية
        print("\n📌 جدول مرجعي:")
        print("   أقل من 18.5  → نقص في الوزن")
        print("   18.5 - 24.9  → وزن طبيعي")
        print("   25.0 - 29.9  → زيادة في الوزن")
        print("   30.0 أو أكثر → سمنة")

except ValueError:
    print("❌ خطأ: يرجى إدخال أرقام صحيحة فقط!")
