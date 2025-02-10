EXECUÇÃO =
VAR
DataMinima = CALCULATE(MIN(fCronograma[DATA
ATUALIZAÇÃO]), ALL(fCronograma))
VAR
DataMaxima = CALCULATE(MAX(fCronograma[DATA
ATUALIZAÇÃO]), ALL(fCronograma))

RETURN
IF(
    MAX(fCronograma[DATA
ATUALIZAÇÃO]) < DataMinima | | MAX(fCronograma[DATA
ATUALIZAÇÃO]) > DataMaxima,
BLANK(),
VAR
SomaExecucao = CALCULATE(
    SUM(fCronograma[EXECUÇÃO]),
    FILTER(
        ALLSELECTED('dCalendario'),
        'dCalendario'[Data] <= MAX(fCronograma[DATA
ATUALIZAÇÃO])
)
)
VAR
SomaHParcial = CALCULATE(
    SUM(fCronograma[H.H
PARCIAL]),
FILTER(
    ALLSELECTED('dCalendario'),
    'dCalendario'[Data] <= MAX(fCronograma[DATA
ATUALIZAÇÃO])
)
)
VAR
Resultado = DIVIDE(SomaExecucao, SomaHParcial, 0)

RETURN
IF(SomaExecucao=0 & & SomaHParcial = 0, 0, Resultado)