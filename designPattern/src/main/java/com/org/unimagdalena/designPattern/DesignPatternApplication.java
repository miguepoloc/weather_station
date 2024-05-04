package com.org.unimagdalena.designPattern;

import com.org.unimagdalena.designPattern.web.api.model.NodeStorageResponse;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DesignPatternApplication {

	public static void main(String[] args) {
		SpringApplication.run(DesignPatternApplication.class, args);
		System.out.println("Estacion Meteorologica en funcionamiento...");
	}

}