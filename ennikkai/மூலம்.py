import re
from pkg_resources import resource_filename as கோப்புபெயர்
import json as ஜேஸான்


கோப்பு_தகவல்கள் = கோப்புபெயர்('ennikkai', 'தகவல்கள்.json')
with open(கோப்பு_தகவல்கள், encoding='utf8') as கோ:
    தகவல்கள் = ஜேஸான்.load(கோ)


def எண்ணுக்கு(உரை):
    """
    Esta función toma texto de un número en cualquier idioma y lo cambia a un número Python.

    :param: El texto a convertir.
    :type உரை: str

    :return: El número de Python correspondiendo
    :rtype: float

    """

    for lengua, d_l in dic_trads.items():
        # Intentar cada lengua disponible.

        l_sep_dec = d_l['sep_dec']  # El separador de decimales
        if not isinstance(l_sep_dec, list):
            l_sep_dec = [l_sep_dec]

        l_núms = list(d_l['núms'])  # Los números

        # Ver si hay posibilidad de un sistema de bases
        try:
            bases = d_l['bases']
        except KeyError:
            bases = None

        # Intentar traducir literalmente, número por número
        for சதம_பிரி in l_sep_dec:
            try:
                núm = _உரை_மொழிபெயர்ப்பு(உரை=உரை, ப_எண்கள்=l_núms, சதம_பிரி=சதம_பிரி)
                # ¿Funcionó? ¡Perfecto!
                return núm if சதம_பிரி in உரை else int(núm)
            except ValueError:
                pass  # ¿No funcionó? Qué pena. Ahora tenemos que trabajar.

        if bases is not None:
            # Intentar ver si puede ser un sistema de bases (unidades).

            try:

                # Ver si hay de separar decimales
                try:
                    entero, dec = உரை.split(சதம_பிரி)
                except ValueError:
                    entero = உரை
                    dec = None

                # Expresiones RegEx para esta lengua
                regex_núm = r'[{}]'.format(''.join([n for n in l_núms]))
                regex_unid = r'[{}]'.format(''.join([b[1] for b in bases]))
                regex = r'((?P<núm>{})?(?P<unid>{}|$))'.format(regex_núm, regex_unid)

                # Intentar encontrar secuencias de unidades y de números en el உரை.
                m = re.finditer(regex, entero)
                resultados = [x for x in list(m) if len(x.group())]

                if not len(resultados):
                    # Si no encontramos nada, seguir con la próxima lengua
                    continue

                # Grupos de números y de sus bases (unidades)
                grupos = resultados[:-1]

                # Dividir en números y en unidades
                núms = [_உரை_மொழிபெயர்ப்பு(g.group('núm'), ப_எண்கள்=l_núms, சதம_பிரி=சதம_பிரி) for g in grupos]
                unids = [_உரை_மொழிபெயர்ப்பு(g.group('unid'), ப_எண்கள்=[b[1] for b in bases], சதம_பிரி=சதம_பிரி)
                         for g in grupos]

                # Calcular el valor de cada número con su base.
                vals = [núms[i] * u for i, u in enumerate(unids)]

                # Agregar o multiplicar valores, como necesario.
                val_entero = vals[0]
                for i, v in enumerate(vals[1:]):
                    if unids[i + 1] > unids[i]:
                        val_entero *= v
                    else:
                        val_entero += v

                # Calcular el número traducido
                if dec is not None:
                    # Si había decima, convertir el உரை decimal
                    val_dec = _உரை_மொழிபெயர்ப்பு(உரை=dec, ப_எண்கள்=l_núms, சதம_பிரி=சதம_பிரி, திரும்பி_உரை=True)

                    # Calcular el número
                    núm = float(str(val_entero) + சதம_பிரி + val_dec)

                else:
                    # ... si no había decimal, no hay nada más que hacer
                    núm = int(val_entero)

                return núm  # Devolver el número

            except (KeyError, ValueError):
                # Si no funcionó, intentemos otra lengua
                pass

    # Si ninguna de las lenguas funcionó, hubo error.
    raise ValueError('No se pudo decifrar el número %s' % உரை)


def உரைக்கு(எண், மொழி):

    if isinstance(எண், str):
        எண்_மூலம் = எண்ணுக்கு(எண்)
    else:
        எண்_மூலம் = எண்


def _உரை_மொழிபெயர்ப்பு(உரை, ப_எண்கள், சதம_பிரி, திரும்பி_உரை=False):
    """
    Esta función traduce un texto a un valor numérico o de texto (formato latino).

    :param உரை: மூல் உரை.
    :type உரை: str
    :param ப_எண்கள்: La lista, en orden ascendente, de los carácteres que corresponden a los números 0, 1, 2, ... 9.
    :type ப_எண்கள்: list[str]
    :param சதம_பிரி: சதம பிரிப்பான்
    :type சதம_பிரி: str
    :param திரும்பி_உரை: Si hay que devolver en formato de texto
    :type திரும்பி_உரை: bool
    :return: El número convertido.
    :rtype: float | str
    """

    if all([அ in ப_எண்கள் + [சதம_பிரி] for அ in உரை]):
        # Si todos los carácteres en el உரை están reconocidos...

        # Cambiar el separador de decimal a un punto.
        உரை = உரை.replace(சதம_பிரி, '.')

        for எ, ஏ in enumerate(ப_எண்கள்):
            # Reemplazar todos los números también.
            உரை = உரை.replace(ஏ, str(எ))

        # Devolver el resultado, o en உரை, o en formato numeral.
        if திரும்பி_உரை:
            return உரை
        else:
            return float(உரை)

    else:
        # Si no se reconocieron todos los carácteres, no podemos hacer nada más.
        raise ValueError('"{}" என்று உரையை படிக்க தெரியாது.'.format(உரை))


