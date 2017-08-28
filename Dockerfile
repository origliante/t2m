FROM centos:centos7
MAINTAINER No one <no-one@no-one.com>

#RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all
RUN yum -y update python; yum clean all

RUN mkdir -p /src
ADD ./t2m.py /src

#RUN cd /src; pip install -r requirements.txt

EXPOSE 1999

CMD ["python", "/src/t2m.py", "0.0.0.0", "1999"]
