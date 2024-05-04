package com.org.unimagdalena.designPattern.domain;

import jakarta.persistence.*;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "nodes_storage")
public class NodeStorageEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "created_at")
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @Column(name = "deleted_at")
    private LocalDateTime deletedAt;

    @Column(name = "is_active")
    private Boolean isActive;

    @Column(name = "date_time")
    private LocalDateTime dateTime;

    @Column(name = "temperature")
    private BigDecimal temperature;

    @Column(name = "humidity")
    private BigDecimal humidity;

    @Column(name = "pressure")
    private BigDecimal pressure;

    @Column(name = "altitude")
    private BigDecimal altitude;

    @Column(name = "node_id")
    private BigDecimal nodeId;

    @Column(name = "battery_level")
    private BigDecimal batteryLevel;

    @Column(name = "conductivity_soil")
    private BigDecimal conductivitySoil;

    @Column(name = "humidity_hd38")
    private BigDecimal humidityHd38;

    @Column(name = "humidity_soil")
    private BigDecimal humiditySoil;

    @Column(name = "nitrogen_soil")
    private BigDecimal nitrogenSoil;

    @Column(name = "ph_soil")
    private BigDecimal phSoil;

    @Column(name = "phosphorus_soil")
    private BigDecimal phosphorusSoil;

    @Column(name = "potassium_soil")
    private BigDecimal potassiumSoil;

    @Column(name = "temperature_soil")
    private BigDecimal temperatureSoil;

}