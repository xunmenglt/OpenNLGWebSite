FROM openjdk:8

MAINTAINER liuteng

VOLUME /tmp

ADD pageserver.jar app.jar

EXPOSE 3000

ENTRYPOINT ["java","-jar","app.jar"]