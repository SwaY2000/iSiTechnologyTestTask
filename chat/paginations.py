from rest_framework import pagination


class CustomThreadOwnerList(pagination.PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'
