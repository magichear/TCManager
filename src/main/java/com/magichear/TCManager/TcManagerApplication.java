package com.magichear.TCManager;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.magichear.TCManager.mapper")
public class TcManagerApplication {

	public static void main(String[] args) {
		SpringApplication.run(TcManagerApplication.class, args);
	}

}
