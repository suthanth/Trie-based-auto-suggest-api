from rest_framework.response import Response
from rest_framework.views import APIView

from trie_search.trie_search_api.service import Trie


class AutoSuggest(APIView):

    def get(self, request):
        search_key = str(request.GET.get('search_key')).lower()
        keys = []
        with open('File.txt') as datafile:
            for row in datafile:
                keys.append(row.lower())

        t = Trie()
        t.form_trie(keys)
        word_list = t.get_auto_suggestions(search_key)

        if word_list == 0:
            return Response(
                data="No words found"
            )

        if word_list == -1:
            return Response(
                data="No other words suggestions found"
            )

        return Response(
            data=word_list
        )
