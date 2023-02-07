class Pagination:
    def __init__(self, limit, object_paginate, page):
        self.limit = limit
        self.object_paginate = object_paginate
        self.page = page

    def do_paginate(self):
        result = self.object_paginate[self.limit * (self.page - 1): self.limit * self.page]
        return result

    def max_page(self):
        max_page = self.object_paginate.__len__() / self.limit
        if round(max_page) < max_page:
            max_page = round(max_page)+1
            return int(max_page)
        return int(round(max_page))


