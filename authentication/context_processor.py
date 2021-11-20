from django.contrib.auth.models import User
from .models import RegistrationStage


def stage(request):
    if request.user.is_authenticated:
        reg_stage = RegistrationStage.objects.get(user=request.user)
        if (reg_stage.stage == '1'):
            print(1)
            return {
                'stage': reg_stage.stage,
                'slug': reg_stage.slug
            }
        elif (reg_stage.stage == '2'):
            print(1)
            return {
                'stage': reg_stage.stage,
                'slug': reg_stage.slug
            }
        return {
            'stage': reg_stage.stage,
        }
    return {
        'stage': 0
    }
