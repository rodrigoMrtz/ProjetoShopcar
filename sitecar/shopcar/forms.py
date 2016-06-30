from haystack.forms import SearchForm


class VeiculosSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()