package com.org.unimagdalena.designPattern.web.api.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@AllArgsConstructor
@Builder
public class NodeStorageResponse {

    private Long id;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private LocalDateTime deletedAt;
    private Boolean isActive;
    private LocalDateTime dateTime;
    private BigDecimal temperature;
    private BigDecimal humidity;
    private BigDecimal pressure;
    private BigDecimal altitude;
    private BigDecimal nodeId;
    private BigDecimal batteryLevel;
    private BigDecimal conductivitySoil;
    private BigDecimal humidityHd38;
    private BigDecimal humiditySoil;
    private BigDecimal nitrogenSoil;
    private BigDecimal phSoil;
    private BigDecimal phosphorusSoil;
    private BigDecimal potassiumSoil;
    private BigDecimal temperatureSoil;

}