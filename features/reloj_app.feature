 Feature: Reloj Alarma

  Scenario: Suena la alarma en el mismo momento
    Given alarma esta "07:00"
    When  hora es "07:00"
     Then suena la alarma 

