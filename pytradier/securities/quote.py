import os
from ..base import Base
from ..const import API_PATH

class Quote(Base):
    '''Super class for quotes'''
    def __init__(self, *symbols):
        Base.__init__(self)

        self._endpoint = os.environ['API_ENDPOINT']
        self._symbols = []

        for symbol in symbols:
            self._symbols.append(symbol)

        self._symbol_load = ','.join(self._symbols)

        self._payload = {'symbols': self._symbol_load}

        self.__data = self._api_response(endpoint=self._endpoint,
                                      path=API_PATH['quotes'],
                                      payload=self._payload)


    def _api_quote(self, attribute):
        # returns the data from the API response in a dictionary for, {symbol0: data0, symbol1: data1, symbol2: data2}
        response_load = {}

        if len(self._symbols) is 1:
            # if there is only one symbol supplied, add it to the dictionary
            response_load[self.__data['quotes']['quote']['symbol']] = self.__data['quotes']['quote'][attribute]

        else:

            for quote in self.__data['quotes']['quote']:
                # more than one symbol supplied, loop through each one and add the strike price of each
                # option to the response_load dictionary

                response_load[quote['symbol']] = quote[attribute]

        return response_load


    def update_data(self):
        self.__data = self._api_response(endpoint=self._endpoint,
                                         path=API_PATH['quotes'],
                                         payload=self._payload)

        # print self.__data

    def add_symbol(self, symbol, update=True):
        # adds a given symbol to the array of tracked symbols. the `update` parameter chooses whether or not to
        # call the API for new data

        self._symbols.append(symbol)
        self._symbol_load = ','.join(self._symbols)
        self._payload = {'symbols': self._symbol_load}

        if update:
            # update the data if the `update` parameter is true
            self.update_data()


    def symbol(self):
        pass

    def desc(self):
        pass