% GOLAB Laboratorio de Analisis Clinicos

paciente(4776313).
paciente(456654).
paciente(78979789).
paciente(1232313).
paciente(741156).

ordenes_pendientes(ot_3).
ordenes_pendientes(ot_4).
ordenes_pendientes(ot_5).
ordenes_pendientes(ot_6).
ordenes_pendientes(ot_7).

medico(4588787).
medico(3333333).
medico(4444444).

ordenes_finalizadas(ot_1).
ordenes_finalizadas(ot_2).


% VERIFICA QUE UN PACIENTE EXISTA - CONTROL REALIZADO ANTES DE CARGAR LA ORDEN DE ANALISIS
cargar_orden_analisis(Cedula) :- paciente(Cedula).

% VERIFICA EL ESTADO DE LA ORDEN - CONTROL REALIZADO ANTES DE ATENDER LA ORDEN DE ANALISIS
verificar_orden(Orden) :-  ordenes_pendientes(Orden).

% VERIFICA QUE UN MEDICO NO EXISTA - CONTROL REALIZADO ANTES DE CARGAR UN MEDICO - NO PUEDE TENER EL MISMO CODIGO
cargar_medico(Codigo) :-  not(medico(Codigo)).

% VERIFICA QUE LA ORDEN SE ENCUENTRE PENDIENTE Y QUE EXISTA EL MEDICO - CONTROL REALIZADO ANTES DE CARGAR UNA ORDEN DE ANALISIS
atender_orden(Orden, Codigo) :- ( verificar_orden(Orden), medico(Codigo) ).

