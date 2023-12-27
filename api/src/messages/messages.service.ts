import { Injectable, InternalServerErrorException } from '@nestjs/common';
import { CreateMessageDto } from './dto/create-message.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { MessageEntity } from './entities/message.entity';
import { Repository } from 'typeorm';
import { KeyWordService } from 'src/key-word/key-word.service';
import { GroupService } from 'src/group/group.service';

@Injectable()
export class MessagesService {
  constructor(
    @InjectRepository(MessageEntity)
    private repository: Repository<MessageEntity>,
    private keyWordService: KeyWordService,
    private groupService: GroupService,
  ) {}
  async findAll() {
    try {
      return await this.repository.find();
    } catch (error) {
      throw new InternalServerErrorException(`Error: ${error}`);
    }
  }
  async createMessage(createMessageDto: CreateMessageDto) {
    try {
      const keyWord = await this.keyWordService.findOne(
        createMessageDto.keyWord,
      );
      const group = await this.groupService.findOne(createMessageDto.groupLink);
      return this.repository.save({
        comment: createMessageDto.comment,
        date: createMessageDto.date,
        group: group,
        hasReplies: createMessageDto.hasReplies,
        keyWord: keyWord,
        name: createMessageDto.name,
        username: createMessageDto.username,
      });
    } catch (error) {
      throw new InternalServerErrorException(`Error: ${error}`);
    }
  }
  async deleteAll() {
    try {
      const messages = await this.findAll();
      messages.forEach(async (message) => {
        await this.repository.delete(message);
      });
      return { success: true };
    } catch (error) {
      throw new InternalServerErrorException(`Error: ${error}`);
    }
  }
}
