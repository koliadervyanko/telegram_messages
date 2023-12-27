import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MessagesModule } from './messages/messages.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { GroupModule } from './group/group.module';
import { LocationModule } from './location/location.module';
import { KeyWordModule } from './key-word/key-word.module';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 7777,
      username: 'postgres',
      password: 'retro_car2010',
      database: 'telegram_messages',
      entities: [__dirname + '/**/*.entity{.js, .ts}'],
      synchronize: true,
    }),
    MessagesModule,
    GroupModule,
    LocationModule,
    KeyWordModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
