from rest_framework import serializers, status

from .models import Thread, Message


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

    def validate_participants(self, value):
        if len(value) != 2:
            raise serializers.ValidationError("Participants must be 2 users")
        if value[0] == value[1]:
            raise serializers.ValidationError("Participants must be different users")
        return value

    def create(self, validated_data):
        participants = validated_data.get('participants')
        if thread := Thread.objects.filter(participants=participants[0]).filter(participants=participants[1]).first():
            self.status_code = status.HTTP_200_OK
            return thread
        thread = Thread.objects.create()
        for participant in participants:
            thread.participants.add(participant)
        thread.save()
        self.status_code = status.HTTP_201_CREATED
        return thread


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def validate(self, data):
        if data.get('thread').participants.filter(id=data.get('sender').id).exists():
            return data
        raise serializers.ValidationError('You cannot send a message to this thread.')

    def create(self, validated_data):
        message = Message.objects.create(thread=validated_data.get('thread'),
                                         sender=validated_data.get('sender'),
                                         text=validated_data.get('text'),
                                         )
        message.save()
        return message
