from rest_framework import exceptions, serializers, status
from rest_framework.serializers import SerializerMethodField


from users.models import User, ActivityPeriod



class UserSerializer(serializers.ModelSerializer):
    activity_period = serializers.SerializerMethodField()

    def get_activity_period(self,obj):
        qs = obj.activity_period.values("start_time","end_time")
        serializer = ActivityPeriodSerializer(qs, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_period')

    def create(self,validated_data):
        request = self.context.get("request",None)
        activity_period_ = request.data.pop('activity_period')
        print(activity_period_)
        user    = User.objects.create(**validated_data)
        for activity_period in activity_period_:
            activity_period_object = ActivityPeriod.objects.create(start_time=activity_period['start_time'],end_time=activity_period['end_time'],user=user)
        user.save()
        return user


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('id', 'start_time', 'end_time')