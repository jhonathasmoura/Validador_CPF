import pytest
from validador_cpf import calcula_dv1, calcula_dv2, valida_cpf, adiciona_mascara_cpf


def test_calcula_dv1():
    assert calcula_dv1("526147915") == 0
    assert calcula_dv1("366256731") == 8
    assert calcula_dv1("168541324") == 2
    assert calcula_dv1("099686269") == 2
    assert calcula_dv1("015529440") == 7
    assert calcula_dv1("833655609") == 5


def test_calcula_dv2():
    assert calcula_dv2("5261479150") == 4
    assert calcula_dv2("3662567318") == 8
    assert calcula_dv2("1685413242") == 8
    assert calcula_dv2("0996862692") == 9
    assert calcula_dv2("0155294407") == 7
    assert calcula_dv2("8336556095") == 5


def test_valida_cpf():
    assert valida_cpf("52614791504")
    assert valida_cpf("36625673188")
    assert valida_cpf("16854132428")
    assert valida_cpf("09968626929")
    assert valida_cpf("01552944077")
    assert valida_cpf("83365560955")

    assert not valida_cpf("25054348163")
    assert not valida_cpf("05274142637")
    assert not valida_cpf("13057727170")
    assert not valida_cpf("00000000000")
    assert not valida_cpf("33333333333")
    assert not valida_cpf("99999999999")


def test_adiciona_mascara_cpf():
    assert adiciona_mascara_cpf("52614791504") == "526.147.915-04"
    assert adiciona_mascara_cpf("36625673188") == "366.256.731-88"
    assert adiciona_mascara_cpf("16854132428") == "168.541.324-28"
    assert adiciona_mascara_cpf("09968626929") == "099.686.269-29"
    assert adiciona_mascara_cpf("01552944077") == "015.529.440-77"
    assert adiciona_mascara_cpf("83365560955") == "833.655.609-55"


if __name__ == "__main__":
    pytest.main()
