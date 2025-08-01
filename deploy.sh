    - name: SSH into EC2 and deploy with Docker Compose
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USERNAME }}
        key: ${{ secrets.EC2_KEY }}
        script: |
          cd /home/ubuntu/app
          chmod +x deploy.sh
          ./deploy.sh
