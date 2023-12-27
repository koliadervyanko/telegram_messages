import { Module } from '@nestjs/common';
import { MessagesService } from './messages.service';
import { MessagesController } from './messages.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { MessageEntity } from './entities/message.entity';
import { KeyWordModule } from 'src/key-word/key-word.module';
import { GroupModule } from 'src/group/group.module';

@Module({
  controllers: [MessagesController],
  providers: [MessagesService],
  imports: [
    TypeOrmModule.forFeature([MessageEntity]),
    KeyWordModule,
    GroupModule,
  ],
})
export class MessagesModule {}
