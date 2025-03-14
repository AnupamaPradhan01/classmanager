# student/models.py
from accounts.models import CustomUser
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="teacher_profile"
    )
    full_name = models.CharField(max_length=150, default="Unknown")
    subject_specialization = models.CharField(max_length=100, default="Not Specified")
    assigned_classes = models.CharField(max_length=100, default="Not Assigned")
    phone_number = models.CharField(max_length=15, default=000000)
    profile_photo = models.ImageField(
        upload_to="teacher_photos/", blank=True, null=True
    )

    def get_assigned_classes(self):
        return self.assigned_classes.split(",")

    def get_subject_specialization(self):
        return self.subject_specialization.split(",")

    def __str__(self):
        return f"{self.user.username} - {self.full_name or 'No Name'}"


class Timetable(models.Model):
    DAYS_OF_WEEK = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]

    TIME_SLOTS = [
        ("7:30 - 8:30", "7:30 - 8:30"),
        ("8:30 - 9:30", "8:30 - 9:30"),
        ("9:30 - 10:30", "9:30 - 10:30"),
        ("11:00 - 11:50", "11:00 - 11:50"),
        ("11:50 - 12:40", "11:50 - 12:40"),
        ("12:40 - 1:30", "12:40 - 1:30"),
        ("2:30 - 3:30", "2:30 - 3:30"),
        ("3:30 - 4:30", "3:30 - 4:30"),
        ("4:30 - 5:30", "4:30 - 5:30"),
    ]

    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_timetables"
    )
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    time_slot = models.CharField(max_length=20, choices=TIME_SLOTS)
    subject = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)

    class Meta:
        unique_together = (
            "day",
            "time_slot",
            "class_name",
        )  # Prevent duplicate time slots per class

    def __str__(self):
        return f"{self.class_name} | {self.day} | {self.time_slot} | {self.subject}"


class Attendance(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="attendance_records"
    )
    class_name = models.CharField(max_length=50)  # Example: "10-A"
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=[("Present", "Present"), ("Absent", "Absent")]
    )

    subject = models.CharField(
        max_length=100,
        choices=[
            ("Math", "Math"),
            ("Science", "Science"),
            ("English", "English"),
        ],
        default="English",  # Modify as needed
    )

    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="marked_attendance"
    )

    def __str__(self):
        return (
            f"{self.class_name} - {self.student.username} - {self.date} - {self.status}"
        )


class Assignment(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assignments"
    )
    title = models.CharField(max_length=255)
    description = RichTextField()  # Updated field
    deadline = models.DateTimeField()
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.class_name})"


class Submission(models.Model):
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name="submissions"
    )
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="submissions"
    )
    submission_file = models.FileField(upload_to="assignments/submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.username}"


class ExamSchedule(models.Model):
    teacher = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="scheduled_exams"
    )
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(null=True, blank=True)
    question_paper = models.FileField(upload_to="exam_papers/", null=True, blank=True)

    def __str__(self):
        return f"{self.class_name} - {self.subject} ({self.exam_date})"

    # Optional validation to ensure the teacher schedules exams only for their assigned classes
    def clean(self):
        if self.class_name not in self.teacher.teacher_profile.assigned_classes.split(
            ","
        ):
            raise ValidationError(
                "Teacher can only schedule exams for their assigned classes."
            )
