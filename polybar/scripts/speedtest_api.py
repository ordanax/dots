#! /usr/bin/env python
#
# Copyright © 2017 white <teo.nespoulet@gmail.com>
#
# Distributed under terms of the MIT license.
import speedtest
s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
result_doct = s.results.dict()
dl_converter = float(result_doct['download'] / 1000000)
up_converter = float(result_doct['upload']   / 1000000)
#print('\uf0ab {0:.3f} Mbps \uf0aa {1:.3f} Mbps \uf111 {2:.0f}   '.format(dl_converter,up_converter, result_doct['ping']))
print('     {2:.0f}   '.format(dl_converter,up_converter,result_doct['ping']))
