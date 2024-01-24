package org.lin.testfeign.client;

import feign.Contract;
import feign.Feign;
import feign.codec.Decoder;
import feign.codec.Encoder;
import org.lin.testfeign.dto.CommonResp;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;



public interface RandomInfoFeignClient {

    @GetMapping("/random/idcard")
    public CommonResp randomIdCard(@RequestParam(name = "count", required = false, defaultValue = "10") String count,
                                   @RequestParam(name = "sex", required = false) String sex,
                                   @RequestParam(name = "birthday", required = false, defaultValue = "yyyy-MM-dd") String birthday,
                                   @RequestParam(name = "nameSuffix", required = false, defaultValue = "") String nameSuffix);

    @GetMapping("/random/phone")
    public CommonResp randomPhone();

    @Component
    class RandomInfoFeignClientConfig {

        @Bean
        public RandomInfoFeignClient randomInfoFeignClient(Decoder decoder, Encoder encoder, Contract contract) {
            return Feign.builder().decoder(decoder).encoder(encoder).contract(contract)
                    .target(RandomInfoFeignClient.class, "http://localhost:8098/");
        }

    }
}
