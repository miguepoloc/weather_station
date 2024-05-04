package com.org.unimagdalena.designPattern.service.impl;

import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import org.springframework.stereotype.Component;

@Component
public class TemperatureHandler extends BaseAlertHandlerImpl{

    @Override
    public String handleRequest(NodeStorageResponse nodeStorageResponse) {
        if (nodeStorageResponse.getTemperature().intValue() > 30) {
            return String.valueOf("Precaucion: Nivel de temperatura alta. Temperatura: " + nodeStorageResponse.getTemperature().intValue() + "C");
        } else {
            if (nextHandler != null) {
                return nextHandler.handleRequest(nodeStorageResponse);
            }
        }
        return null;
    }

}
