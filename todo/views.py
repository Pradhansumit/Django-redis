# for deserializing the data
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import TodoModel
from todo.serializer import TodoSerializer


class CreateView(APIView):
    def post(self, request, format=None) -> Response:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ListView(APIView):
    def get(self, request) -> Response:
        try:
            todos = TodoModel.objects.all().values()
            print(TodoModel.objects.all())
            return Response(todos, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class ListDetailView(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        todo_id = kwargs["pk"]

        if cache.get(todo_id):
            todo = cache.get(todo_id)
            print("getting data from the cached files")
            print(todo) if todo else ""
            # serialized_obj = serializers.serialize('json', [todo,])
            # todo_json = todo.values()
            # print(serialized_obj)
            # return Response(serialized_obj)
        else:
            try:
                todo = TodoModel.objects.get(pk=todo_id)
                cache.set(
                    todo_id,
                    todo,
                )
                print("new cache has been set")
                return Response(todo.values())
            except Exception as e:
                print(str(e))
        return Response()


class DeleteView(APIView):
    def get(self, request, *args, **kwargs):
        todo_id = kwargs["pk"]
        todo = TodoModel.objects.get(pk=todo_id)
        print(todo)
        if todo is not None:
            todo.delete()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
