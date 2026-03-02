# استخدام نسخة بايثون مستقرة وخفيفة
FROM python:3.12-slim

# ضبط متغيرات البيئة لمنع بايثون من كتابة ملفات .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# تثبيت الاعتماديات الأساسية للنظام
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# نسخ ملف المتطلبات أولاً لتحسين سرعة البناء
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# تشغيل عمليات الجمع للملفات الساكنة (Static)
RUN python manage.py collectstatic --noinput

# فتح المنفذ 8000
EXPOSE 8000

# أمر التشغيل (استخدام gunicorn للإنتاج)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application"]