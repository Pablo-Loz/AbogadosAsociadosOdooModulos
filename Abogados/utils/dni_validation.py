from odoo.exceptions import ValidationError
import re

def is_valid_dni(dni):
    """
    Valida un DNI español.

    :param dni: El DNI a validar.
    :return: True si el DNI es válido, False de lo contrario.
    """
    if len(dni) != 9:
        return False
    if not dni[:8].isdigit() or not dni[-1].isalpha():
        return False

    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    numero = int(dni[:8])
    letra = dni[-1].upper()
    return letras[numero % 23] == letra

def is_valid_cif(cif):
    """
    Valida un CIF español.

    :param cif: El CIF a validar.
    :return: True si el CIF es válido, False de lo contrario.
    """
    cif = cif.upper()
    if not re.match(r'^[ABCDEFGHJKLMNPQRSUVW]\d{7}[0-9A-J]$', cif):
        return False

    letras = 'JABCDEFGHI'
    control = cif[-1]

    if control.isdigit():
        control = int(control)
    else:
        control = letras.index(control)

    suma_pares = sum(int(cif[i]) for i in range(2, 8, 2))
    suma_impares = sum(sum(divmod(2 * int(cif[i]), 10)) for i in range(1, 9, 2))
    total = suma_pares + suma_impares

    if cif[0] in 'ABEH':
        return control == (10 - total % 10) % 10
    if cif[0] in 'KPQS':
        return control == letras[total % 10]
    return control in {str((10 - total % 10) % 10), letras[total % 10]}

def is_valid_nie(nie):
    """
    Valida un NIE español.

    :param nie: El NIE a validar.
    :return: True si el NIE es válido, False de lo contrario.
    """
    nie = nie.upper()
    if len(nie) != 9:
        return False
    if not re.match(r'^[XYZ]\d{7}[A-Z]$', nie):
        return False

    conversion = {'X': '0', 'Y': '1', 'Z': '2'}
    nie = conversion[nie[0]] + nie[1:]
    return is_valid_dni(nie)

def validate_dni(dni):
    """
    Verifica que el DNI, CIF o NIE cumple con los requisitos y lanza una excepción si no es válido.

    :param dni: El DNI, CIF o NIE a validar.
    :raises ValidationError: Si el DNI, CIF o NIE no es válido.
    """
    if not dni:
        raise ValidationError('El campo de identificación no puede estar vacío.')

    dni = dni.upper()

    if len(dni) != 9:
        raise ValidationError('El campo de identificación debe tener exactamente 9 caracteres.')

    if not (is_valid_dni(dni) or is_valid_cif(dni) or is_valid_nie(dni)):
        raise ValidationError('El campo de identificación no es válido.')
