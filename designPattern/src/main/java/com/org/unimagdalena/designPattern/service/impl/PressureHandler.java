package com.org.unimagdalena.designPattern.service.impl;

import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import org.springframework.stereotype.Component;

@Component
public class PressureHandler extends BaseAlertHandlerImpl{

    @Override
    public String handleRequest(NodeStorageResponse nodeStorageResponse) {
        if (nodeStorageResponse.getPressure().intValue() < 1000) {
            return String.valueOf("Precaucion: Nivel de presion baja. Presion: " + nodeStorageResponse.getPressure().intValue() + "hPa");
        } else {
            if (nextHandler != null) {
                return nextHandler.handleRequest(nodeStorageResponse);
            }
        }
        return null;
    }
}
