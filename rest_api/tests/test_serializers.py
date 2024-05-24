import pytest
from base.models import Petshop
from rest_api.serializersReservaModelSerializer, 


def dados_agendamento_invalido():
 ontem = datetime.date.today() - datetime
 return {
  'nome' : '<NAME>',
  'email': '<EMAIL>',
  'nome_pet': 'body',
  'turno': 'manha',
  'tamanho': '5',
  'obs': '',
  'data': ontem,
  'petshop': petshop.pk

 }
@pytest.mark.django_db
def test_dados_agendamento_incorreto():
        serializer = ReservaModelSerializer(data=dados_agendamento_invalido)
        assert not serializer.is_valid()