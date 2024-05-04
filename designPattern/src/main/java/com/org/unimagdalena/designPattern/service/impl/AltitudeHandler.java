package com.org.unimagdalena.designPattern.service.impl;

import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import org.springframework.stereotype.Component;

@Component
public class AltitudeHandler extends BaseAlertHandlerImpl{

    @Override
    public String handleRequest(NodeStorageResponse nodeStorageResponse) {
        if (nodeStorageResponse.getAltitude().intValue() < 20) {
            return String.valueOf("Precaucion: Altitud del nodo muy baja. Altitud: " + nodeStorageResponse.getAltitude().intValue() + "m");
        } else {
            return String.valueOf("Estacion Meteorologica en excelente estado.");
        }
    }
}