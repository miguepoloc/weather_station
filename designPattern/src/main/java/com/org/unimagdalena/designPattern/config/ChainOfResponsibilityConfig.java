package com.org.unimagdalena.designPattern.config;

import com.org.unimagdalena.designPattern.service.impl.AltitudeHandler;
import com.org.unimagdalena.designPattern.service.impl.HumidityHandler;
import com.org.unimagdalena.designPattern.service.impl.PressureHandler;
import com.org.unimagdalena.designPattern.service.impl.TemperatureHandler;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class ChainOfResponsibilityConfig {

    @Autowired
    public void configureHandlers(
            TemperatureHandler temperatureHandler,
            HumidityHandler humidityHandler,
            PressureHandler pressureHandler,
            AltitudeHandler altitudeHandler
    ) {
        temperatureHandler.setNextHandler(humidityHandler);
        humidityHandler.setNextHandler(pressureHandler);
        pressureHandler.setNextHandler(altitudeHandler);
    }

}
