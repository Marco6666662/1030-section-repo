# CircuitMart Project

CircuitMart is an e-commerce website where you can buy computer parts and accessories. CircuitMart offers a wide range of computer parts, including CPUs, graphics cards, motherboards, RAM, storage devices, and more, from reputable brands. Revenue streams for CircuitMart comes from commissions on sales, subscription fees, advertising, and data monetization. CircuitMart aims to provide a convenient and efficient shopping experience for tech enthusiasts looking to build or upgrade their computer systems. The website also offers “non-tech savvy” buyers a form where they can find part that are best option for them. With CircuitMart, buyers can easily find the parts they need to build or upgrade their computer systems.


This repo contains a setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for the CircuitMart database
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server for the CircuitMart website

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 
