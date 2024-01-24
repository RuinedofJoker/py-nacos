package org.lin.testfeign;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.openfeign.EnableFeignClients;

@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients(basePackages = {"org.lin.testfeign.client"})
public class TestFeignApplication {

    public static void main(String[] args) {
        SpringApplication.run(TestFeignApplication.class, args);
    }

}
