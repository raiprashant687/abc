import pytest
import requests
from Pytests_new.utility.csvreader_Info import getdatafromcsv


class Test_getRecordingList:
    @pytest.mark.parametrize('MAC,a,b,c',getdatafromcsv())
    def test_first(self,MAC,a,b,c):
        print(f"{MAC} {a} {b} {c}")
        assert MAC!=None

    @pytest.mark.depends(on=['test_first'])
    def test_second(self):
        assert True

    @pytest.mark.parametrize('MAC,a,b,c',getdatafromcsv())
    def checkhttpconnection(self,MAC,a,b,c):
        r = requests.get(f"http://10.67.174.30:8085/broker/bta/getRecordingList?MAC={MAC}")
        print(r.status_code)
        assert r.status_code != 200
