package sample.config;

import java.net.InetAddress;
import java.net.UnknownHostException;
import sample.CustomCookieSerializer;

import org.springframework.boot.web.embedded.jetty.JettyServletWebServerFactory;
import org.springframework.boot.web.servlet.server.ServletWebServerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.session.web.http.CookieSerializer;

@Configuration
public class ServletConfig {

    @Bean
    public ServletWebServerFactory servletWebServerFactory() {
        return new JettyServletWebServerFactory();
    }

    @Bean
    public CookieSerializer cookieSerializer() {
        CustomCookieSerializer serializer = new CustomCookieSerializer();
        serializer.setCookieName("JSESSIONID");
        serializer.setCookiePath("/");
        serializer.setPostfix(getPostfix());
        return serializer;
    }

    private String getPostfix() {
        try {
            InetAddress inetAddress = InetAddress.getLocalHost();
            String ip = inetAddress.getHostAddress();
            Integer workerId = Integer.parseInt(ip.substring(ip.lastIndexOf(".") + 1));
            return ".worker" + workerId%4 ;
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
        return "";
    }
}
