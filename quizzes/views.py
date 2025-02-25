from django.shortcuts import render, get_object_or_404
from .models import Quiz, Option


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        score = 0
        total_questions = quiz.questions.count()
        for question in quiz.questions.all():
            selected_option_id = request.POST.get(str(question.id))
            if selected_option_id:
                try:
                    option = Option.objects.get(id=selected_option_id)
                    if option.is_correct:
                        score += 1
                except Option.DoesNotExist:
                    pass
        context = {
            'quiz': quiz,
            'score': score,
            'total_questions': total_questions,
        }
        return render(request, 'quiz_result.html', context)
    else:
        return render(request, 'quiz_detail.html', {'quiz': quiz})
